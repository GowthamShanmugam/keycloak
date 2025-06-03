import Keycloak from 'keycloak-js';

const keycloak = new Keycloak({
  url: 'http://localhost:8080',
  realm: 'rhoai',
  clientId: 'client-app-2'
});

export default keycloak;
