import { useHistory } from "react-router-dom";
import { downloadDataset } from "../../services/DatasetService";
import { useDataSet } from "../../hooks";

const DataSetCard = ({ id, catalog, name, short_description }) => {
  const history = useHistory();
  const { setSelectedDataSet } = useDataSet();

  const onDownload = () => {
    downloadDataset(id).then((r) => console.log(r));
  };

  const navigateDataSetDetails = () => {
    setSelectedDataSet({ id, catalog, name, short_description });
    history.push("/dataset");
  };

  return (
    <div className="datasetcard" onClick={navigateDataSetDetails}>
      <div className="dataset-name">{name}</div>
      <h3>{catalog}</h3>
      <div className="dataset-desc">{short_description}</div>
      <button onClick={onDownload} className="download-button">
        Download
      </button>
    </div>
  );
};

export default DataSetCard;
