import Col from "react-bootstrap/Col";

import { downloadDataset } from "../../services/DatasetService";

const DataSetCard = ({ id, catalog, name, short_description }) => {
  const onDownload = () => {
    downloadDataset(id).then((r) => console.log(r));
  };
  return (
    <Col md={5} className="datasetcard">
      <div className="dataset-name">{name}</div>
      <h3>{catalog}</h3>
      <div className="dataset-desc">{short_description}</div>
      <button onClick={onDownload} className="download-button">
        Download
      </button>
    </Col>
  );
};

export default DataSetCard;
