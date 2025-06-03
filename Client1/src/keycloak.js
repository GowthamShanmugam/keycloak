import Keycloak from 'keycloak-js';

const keycloak = new Keycloak({
  url: 'http://localhost:8080/',
  realm: 'rhoai',
  clientId: 'client-app-1'
});

export default keycloak;
