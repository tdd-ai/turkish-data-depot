import "./App.css";

import { useMemo, useState } from "react";
import { HashRouter as Switch, Route } from "react-router-dom";

import NavigationBar from "./components/NavigationBar";
import StorageService from "./services/StorageService";
import { DataSets, DataSetDetails } from "./screens";
import { AUTH_ROUTES, APP_ADDRESS_URL } from "./constants/Routes";

import { DataSetContext } from "./context";

function App() {
  const [selectedDataSet, setSelectedDataSet] = useState(null);

  const dataSetContext = useMemo(
    () => ({
      selectedDataSet,
      setSelectedDataSet,
    }),
    [selectedDataSet, setSelectedDataSet]
  );

  return (
    <DataSetContext.Provider value={dataSetContext}>
      <Switch>
        <NavigationBar />
        <Route exact path="/">
          <DataSets />
        </Route>
        <Route path="/:id">
          <DataSetDetails />
        </Route>
         <Route path="/login" component={() => {
              window.location = `${AUTH_ROUTES.LOGIN}?redir=${APP_ADDRESS_URL}`
            }} />
          <Route path="/signout" component={() => {
              StorageService.removeAccessToken()
              window.location = `${APP_ADDRESS_URL}`
          }} />
      </Switch>
    </DataSetContext.Provider>
  );
}

export default App;
