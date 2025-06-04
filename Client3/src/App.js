import React from 'react';

const login = async (setState) => {
  const response = await fetch('http://app1.localhost:5003/login', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({
      username: 'rhoai',
      password: 'admin',
    }),
  });

  const data = await response.json();
  setState(data)
};

function App() {
  const [state, setState] = React.useState("");

  return (
    <div>
      <h1>Welcome to the App</h1>
      <button onClick={() =>login(setState)}>Login</button>
      <div>{JSON.stringify(state)}</div>
    </div>
  );
}

export default App;
