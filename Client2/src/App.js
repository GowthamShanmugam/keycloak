import React from 'react';
import { useKeycloak } from '@react-keycloak/web';

function App() {
  const { keycloak, initialized } = useKeycloak();
  const [state, setState] = React.useState("");
  

  if (!initialized) {
    return <div>Loading...</div>;
  }

  

  const callBackend = async () => {
    const token = keycloak.token;

    const response = await fetch('http://app2.localhost:5002/protected', {
      method: 'GET',
      headers: {
        Authorization: `Bearer ${token}`,
      },
    });

    const data = await response.json();
    setState(data);
};


  return (
    <div>
      <h1>Welcome to the App</h1>
      {keycloak.authenticated ? (
        <>
        <>
          <p>Logged in as: {keycloak.tokenParsed?.preferred_username}</p>
          <p>Client id: {keycloak.clientId}</p>
          <button onClick={() => keycloak.logout()}>Logout</button>
        </>
          <>
            <h1>React + Keycloak</h1>
            <button onClick={callBackend}>Call Protected Backend</button>
          </>
          <>
          <div>{JSON.stringify(state)}</div>
          </>
        </>
      ) : (
        <button onClick={() => keycloak.login()}>Login</button>
      )}
    </div>
  );
}

export default App;
