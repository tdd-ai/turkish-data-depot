import "./App.css";

import { HashRouter as Switch, Route } from "react-router-dom";
import styled from "styled-components";

import NavigationBar from "./components/NavigationBar";
import { DataSets } from "./screens";

function App() {
  return (
    <>
      <NavigationBar />
      <Switch>
        <Route path="/">
          <DataSets />
        </Route>
      </Switch>
    </>
  );
}

export default App;
