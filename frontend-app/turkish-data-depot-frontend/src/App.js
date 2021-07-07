import "./App.css";

import { HashRouter as Switch, Route } from "react-router-dom";

import NavigationBar from "./components/NavigationBar";
import { DataSets, DataSetDetails } from "./screens";

function App() {
  return (
    <>
      <NavigationBar />
      <Switch>
        <Route exact path="/">
          <DataSets />
        </Route>
        <Route path="/dataset">
          <DataSetDetails />
        </Route>
      </Switch>
    </>
  );
}

export default App;
