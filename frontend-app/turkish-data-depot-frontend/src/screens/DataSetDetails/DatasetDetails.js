import ReactMarkdown from "react-markdown";
import { DataSetDetailContainer } from "./DataSetDetails.styled";

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
  return (
    <DataSetDetailContainer>
      <h1>Dataset Title</h1>
      <h3>Dataset Details Catalog</h3>
      <p>
        Lorem ipsum dolor sit amet, consectetur adipiscing elit. Curabitur
        auctor, velit eget rhoncus ultricies, nisi nulla condimentum enim, eget
        porta lorem leo eu nunc. Lorem ipsum dolor sit amet, consectetur
        adipiscing elit. Curabitur auctor, velit eget rhoncus ultricies, nisi
        nulla condimentum enim, eget porta lorem leo eu nunc. Lorem ipsum dolor
        sit amet, consectetur adipiscing elit. Curabitur auctor, velit eget
        rhoncus ultricies, nisi nulla condimentum enim, eget porta lorem leo eu
        nunc.
      </p>
      <ReactMarkdown>{markdown}</ReactMarkdown>
    </DataSetDetailContainer>
  );
};

export default DatasetDetails;
