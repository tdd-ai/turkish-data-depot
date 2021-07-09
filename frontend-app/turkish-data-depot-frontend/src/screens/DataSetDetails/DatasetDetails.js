import { useState, useEffect } from "react";

import { useRouteMatch } from "react-router-dom";
import ReactMarkdown from "react-markdown";
import {
  ContentContainer,
  DataSetDetailContainer,
} from "./DataSetDetails.styled";

import { getDataset } from "../../services/FilterService";
import Annotations from "./Annotations";
import FileDetails from "./FileDetails";

const DatasetDetails = () => {
  const {
    params: { id },
  } = useRouteMatch();
  const [dataSet, setDataSet] = useState(null);

  async function fetchDataSet() {
    const response = await getDataset(id);
    setDataSet(response);
  }

  useEffect(() => {
    fetchDataSet();
  }, []);

  return dataSet ? (
    <DataSetDetailContainer>
      {dataSet.annotations && <Annotations annotations={dataSet.annotations} />}
      <ContentContainer>
        <h2>{dataSet.name}</h2>
        <h4>{dataSet.catalog}</h4>
        <p>{dataSet.short_description}</p>
        <ReactMarkdown>{dataSet.description}</ReactMarkdown>
      </ContentContainer>
      <FileDetails dataset={dataSet} />
    </DataSetDetailContainer>
  ) : null;
};

export default DatasetDetails;
