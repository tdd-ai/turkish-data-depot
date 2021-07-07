import { useContext } from "react";
import { DataSetContext } from "../context";

export const useDataSet = () => useContext(DataSetContext);
