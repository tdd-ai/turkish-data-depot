import { FileDetailsContainer } from "./DataSetDetails.styled";
import { downloadDataset } from "../../services/DatasetService";

const FileDetails = ({ dataset }) => {
  const onDownload = () => {
    downloadDataset(dataset.id).then((r) => {
      window.location = r.url;
    });
  };

  return (
    <FileDetailsContainer>
      <h3>Details</h3>
      <table>
        <tbody>
          <tr>
            <th>Name</th>
            <th>{dataset.name}</th>
          </tr>
          <tr>
            <th>Catalog</th>
            <th>{dataset.catalog}</th>
          </tr>
          <tr>
            <th>Description</th>
            <th>{dataset.short_description}</th>
          </tr>
          <tr>
            <th>Version</th>
            <th>{dataset.version}</th>
          </tr>
          <tr>
            <th>Type</th>
            <th>{dataset.type}</th>
          </tr>
          <tr>
            <th>Data Type</th>
            <th>{dataset.data_type}</th>
          </tr>
          <tr>
            <th>Source</th>
            <th>{dataset.source}</th>
          </tr>
          <tr>
            <th>License</th>
            <th>{dataset.license}</th>
          </tr>
          <tr>
            <th>Compression</th>
            <th>{dataset.compression}</th>
          </tr>
          <tr>
            <th>Format</th>
            <th>{dataset.format}</th>
          </tr>
          <tr>
            <th>Download Size</th>
            <th>{dataset.download_size}</th>
          </tr>
          <tr>
            <th>Authors</th>
            <th>{dataset.authors}</th>
          </tr>
          <tr>
            <th>Release Date</th>
            <th>{dataset.release_date}</th>
          </tr>
        </tbody>
      </table>
      <button onClick={onDownload} className="download-button">
        Download Data Set
      </button>
    </FileDetailsContainer>
  );
};

export default FileDetails;
