import { Redirect } from "react-router-dom";
import ReactMarkdown from "react-markdown";
import { DataSetDetailContainer } from "./DataSetDetails.styled";

import { useDataSet } from "../../hooks";

const markdown = `
  # Title
  ## Title
  ### Title
  #### Title
  ##### Title
  ###### Title

  Lorem ipsum dolor si amet.

  > Lorem ipsum dolor si amet.

  ![Image](https://placehold.it/500x500)
`;

const DatasetDetails = () => {
  const { selectedDataSet } = useDataSet();

  return selectedDataSet ? (
    <DataSetDetailContainer>
      <h1>{selectedDataSet.name}</h1>
      <h3>{selectedDataSet.catalog}</h3>
      <p>{selectedDataSet.short_description}</p>
      <ReactMarkdown>{markdown}</ReactMarkdown>
    </DataSetDetailContainer>
  ) : (
    <Redirect to="/" />
  );
};

export default DatasetDetails;
