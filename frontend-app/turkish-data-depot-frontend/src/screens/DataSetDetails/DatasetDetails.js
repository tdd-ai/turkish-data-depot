import { useState, useEffect } from "react";

import { useRouteMatch } from "react-router-dom";
import ReactMarkdown from "react-markdown";
import gfm from "remark-gfm";

import {
  ContentContainer,
  DataSetDetailContainer,
} from "./DataSetDetails.styled";

import { getDataset } from "../../services/FilterService";
import Annotations from "./Annotations";
import FileDetails from "./FileDetails";
import { useRedirectedData } from "../../hooks";

const DatasetDetails = () => {
  const {
    params: { id },
  } = useRouteMatch();
  const [dataSet, setDataSet] = useState(null);

  useRedirectedData();

  const fetchDataSet = async () => {
    const response = await getDataset(id);
    setDataSet(response);
  };

  useEffect(() => {
    fetchDataSet();
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, []);

  return dataSet ? (
    <DataSetDetailContainer>
      {dataSet.annotations && <Annotations annotations={dataSet.annotations} />}
      <ContentContainer>
        <h2>{dataSet.name}</h2>
        <h4>{dataSet.catalog}</h4>
        <ReactMarkdown remarkPlugins={[gfm]} children={dataSet.description} />
      </ContentContainer>
      <FileDetails dataset={dataSet} />
    </DataSetDetailContainer>
  ) : null;
};

export default DatasetDetails;
