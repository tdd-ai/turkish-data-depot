import "./App.css";

import { useMemo, useState } from "react";
import { HashRouter as Switch, Route } from "react-router-dom";

import NavigationBar from "./components/NavigationBar";
import { DataSets, DataSetDetails } from "./screens";

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
      <NavigationBar />
      <Switch>
        <Route exact path="/">
          <DataSets />
        </Route>
        <Route path="/:id">
          <DataSetDetails />
        </Route>
      </Switch>
    </DataSetContext.Provider>
  );
}

export default App;
