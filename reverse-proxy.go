package main

import (
    "log"
    "net/http"
    "net/http/httputil"
    "net/url"
    "strings"
)

func main() {
    http.HandleFunc("/proxy/", func(w http.ResponseWriter, r *http.Request) {
        path := strings.TrimPrefix(r.URL.Path, "/proxy/")
        parts := strings.SplitN(path, "/", 2)
        if len(parts) < 2 {
            http.Error(w, "Invalid path", http.StatusBadRequest)
            return
        }
        serviceName := parts[0]
        servicePath := "/" + parts[1]

        var target *url.URL
        switch serviceName {
        case "service-a":
            target, _ = url.Parse("http://localhost:8001")
        case "service-b":
            target, _ = url.Parse("http://localhost:8002")
        default:
            http.Error(w, "Unknown service", http.StatusBadGateway)
            return
        }

        proxy := httputil.NewSingleHostReverseProxy(target)
        r.URL.Path = servicePath
        r.Host = target.Host
        proxy.ServeHTTP(w, r)
    })

    log.Println("Starting proxy server on :8080")
    log.Fatal(http.ListenAndServe(":8080", nil))
}
