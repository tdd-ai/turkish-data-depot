import { useEffect, useState } from "react";

import { useHistory } from "react-router-dom";

import {
  listAnnotations,
  listCompressions,
  listDatasets,
  listDataTypes,
  listFormats,
  listLicenses,
  listSources,
  listTypes,
} from "../../services/FilterService";
import StorageService from "../../services/StorageService";
import { downloadDataset } from "../../services/DatasetService";

import { DatasetsContainer, DataSetCardsContainer } from "./Datasets.styled";
import Filters from "./Filters";
import DataSetCard from "./DataSetCard";

import { useQuery } from "../../hooks";

const DataSets = () => {
  const query = useQuery();
  const history = useHistory();

  const url = window.location.href;
  const toDownloadId = (/\?id=([\s\S]*)\?token/.exec(url) || [])[1];
  const token = (/\?token=([\s\S]*)/.exec(url) || [])[1];

  if (token) {
    StorageService.saveAccessToken(token);
    query.delete("token");
    history.replace({
      search: query.toString(),
    });
  }

  const [dataTypes, setDataTypes] = useState(null);
  const [annotations, setAnnotations] = useState(null);
  const [sources, setSources] = useState(null);
  const [formats, setFormats] = useState(null);
  const [compressions, setCompressions] = useState(null);
  const [types, setTypes] = useState(null);
  const [licenses, setLicenses] = useState(null);
  const [datasets, setDatasets] = useState(null);
  const [filter, _setFilter] = useState({
    types: [],
    "data-types": [],
    annotations: [],
    sources: [],
    compressions: [],
    licenses: [],
    formats: [],
  });
  const [searchValue, setSearchValue] = useState("");

  const setFilter = (f) => {
    _setFilter(f);
    listDatasets(f).then((r) => setDatasets(r));
  };

  useEffect(() => {
    listDataTypes().then((r) => setDataTypes(r));
    listAnnotations().then((r) => setAnnotations(r));
    listSources().then((r) => setSources(r));
    listFormats().then((r) => setFormats(r));
    listCompressions().then((r) => setCompressions(r));
    listTypes().then((r) => setTypes(r));
    listLicenses().then((r) => setLicenses(r));
    listDatasets().then((r) => {
      setDatasets(r);
    });
    if (toDownloadId) {
      downloadDataset(toDownloadId).then((r) => {
        console.log(r);
      });
    }
  }, [url, toDownloadId]);

  const searchFilter = (d) =>
    searchValue
      ? `${d.name}${d.catalog}${d.short_description}`
          .toLocaleLowerCase()
          .includes(searchValue.toLowerCase())
      : d;

  const onChangeSearch = (e) => {
    setSearchValue(e.target.value);
  };

  return (
    <DatasetsContainer>
      <div className="filters-c">
        <h2 className="datasets-title">Filters</h2>
        <Filters
          title="Types"
          filters={types}
          k={"types"}
          filter={filter}
          setFilter={setFilter}
        />
        <Filters
          title="Data Types"
          filters={dataTypes}
          k={"data-types"}
          filter={filter}
          setFilter={setFilter}
        />
        <Filters
          title="Annotations"
          filters={annotations}
          k={"annotations"}
          filter={filter}
          setFilter={setFilter}
        />
        <Filters
          title="Sources"
          filters={sources}
          k={"sources"}
          filter={filter}
          setFilter={setFilter}
        />
        <Filters
          title="Compression Types"
          filters={compressions}
          k={"compressions"}
          filter={filter}
          setFilter={setFilter}
        />
        <Filters
          title="Licenses"
          filters={licenses}
          k={"licenses"}
          filter={filter}
          setFilter={setFilter}
        />
        <Filters
          title="Formats"
          filters={formats}
          k={"formats"}
          filter={filter}
          setFilter={setFilter}
        />
      </div>
      <div className="datasets-c">
        <div
          style={{
            display: "flex",
            justifyContent: "space-between",
            alignItems: "center",
            marginBottom: 16,
          }}
        >
          <h2 className="datasets-title">Datasets</h2>
          <input
            type="text"
            onChange={onChangeSearch}
            value={searchValue}
            placeholder="Search datasets..."
            className="dataset-search"
          />
        </div>
        <DataSetCardsContainer>
          {datasets?.filter(searchFilter).map((dataset) => (
            <DataSetCard key={dataset.id} {...dataset} />
          ))}
        </DataSetCardsContainer>
      </div>
    </DatasetsContainer>
  );
};

export default DataSets;
