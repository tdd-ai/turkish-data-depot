import { useEffect, useState } from "react";
import styled from "styled-components";
import Tooltip from "react-bootstrap/Tooltip";
import OverlayTrigger from "react-bootstrap/OverlayTrigger";
import Row from "react-bootstrap/Row";
import Col from "react-bootstrap/Col";
import {
  listAnnotations,
  listCompressions,
  listDatasets,
  listDataTypes,
  listFormats,
  listLicenses,
  listSources,
  listTypes,
} from "../services/FilterService";
import StorageService from "../services/StorageService";
import { downloadDataset } from "../services/DatasetService";

const Styles = styled.div`
  display: flex;
  flex-direction: row;
  .filters-c {
    display: flex;
    width: 30%;
    height: 100%;
    padding: 20px 40px;
    flex-direction: column;
  }
  .datasetcard {
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    margin: 10px;
    padding: 12px;
    background: rgba(77, 199, 239, 0.6);
    border-radius: 12px;
    cursor: pointer;
    &:hover {
      background: rgba(77, 199, 239, 0.7);
    }
  }
  .datasets-c {
    width: 70%;
    height: 100%;
    border-left: 1px solid #bec0c2;
  }
  .filter {
    margin: 5px;
    width: fit-content;
    padding: 5px 10px;
    border-radius: 5px;
    cursor: pointer;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 12px;
    line-height: 1.2;
    background-color: rgba(248, 151, 28, 0.3);
    &:hover {
      background-color: rgba(248, 151, 28);
    }
    color: rgba(156, 87, 0);
    font-weight: 500;
  }
  .selected-filter {
    background-color: #f8f8f8;
    color: #9c9c9c;
  }
  .tags-c {
    display: flex;
    flex-direction: row;
    flex-wrap: wrap;
    align-items: center;
    width: 100%;
  }
  .expand {
    font-size: 12px;
    cursor: pointer;
    margin-left: 5px;
    padding: 5px;
    color: rgba(33, 37, 41, 0.8);
    &:hover {
      background-color: #f8f9fa;
      border-radius: 5px;
    }
  }
  .datasets-c {
    padding: 20px 40px;
  }
  h3 {
    font-size: 12px;
    font-weight: bold;
  }
  .dataset-desc {
    overflow: hidden;
    text-overflow: ellipsis;
    display: -webkit-box;
    -webkit-line-clamp: 2; /* number of lines to show */
    -webkit-box-orient: vertical;
    font-size: 12px;
    &:hover {
      -webkit-line-clamp: 12; /* number of lines to show */
    }
  }
  .dataset-name {
    font-weight: bolder;
  }
  .dataset-search {
    font-size: 12px;
    height: 20px;
    border-radius: 12px;
    border: 1px solid #bec0c2;
    padding: 12px;
    &:focus {
      outline: none !important;
      border-color: rgba(77, 199, 239);
    }
  }
  .download-button {
    width: fit-content;
    padding: 5px 10px;
    border-radius: 5px;
    cursor: pointer;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 12px;
    line-height: 1.2;
    background-color: rgba(248, 151, 28);
    &:hover {
      background-color: rgba(248, 151, 28, 0.3);
    }
    color: rgba(156, 87, 0);
    font-weight: 500;
  }
`;

const Filters = ({ title, filters, filter, setFilter, k }) => {
  const [isExpanded, setExpanded] = useState(false);
  const sliceSize = 4;
  if (!filters) {
    return <span style={{ fontWeight: 500, marginBottom: 10 }}>{title}</span>;
  }
  const updateFilter = (e, t) => {
    let toSet = [...filter[k]];
    if (isSelected(e.name)) {
      toSet = toSet.filter((i) => i !== e.name);
    } else {
      toSet.push(e.name);
    }
    setFilter({
      ...filter,
      [k]: toSet,
    });
  };

  const isSelected = (key) => {
    return filter[k].includes(key);
  };
  return (
    <>
      <span style={{ fontWeight: 500, marginBottom: 10 }}>{title}</span>
      <div style={{ marginBottom: 20, width: "100%" }} className="tags-c">
        {(isExpanded ? filters : filters.slice(0, sliceSize)).map((el) => {
          const renderTooltip = (props) => (
            <Tooltip id="button-tooltip" {...props}>
              {el.description}
            </Tooltip>
          );
          return (
            <OverlayTrigger placement="top" overlay={renderTooltip}>
              <div
                onClick={() => {
                  updateFilter(el, title);
                }}
                className={
                  isSelected(el.name) ? "filter" : "selected-filter filter"
                }
              >
                {el.name}
              </div>
            </OverlayTrigger>
          );
        })}
        {filters.length - sliceSize > 0 && (
          <div onClick={() => setExpanded(!isExpanded)} className="expand">
            {isExpanded ? "⇠" : filters.length - sliceSize + " more"}
          </div>
        )}
      </div>
    </>
  );
};

const DatasetCard = ({ id, catalog, name, short_description }) => {
  const onDownload = () => {
    downloadDataset(id).then((r) => {
      let [err, result] = r;
      if (err && err.message === "EXPIRED_TOKEN") {
        return downloadDataset(id); // Already cleared the token, now will redirect to auth
      }
    });
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

const Datasets = () => {
  const url = window.location.href;
  const toDownloadId = (/\?id=([\s\S]*)\?token/.exec(url) || [])[1];
  const token = (/\?token=([\s\S]*)/.exec(url) || [])[1];
  if (token) {
    StorageService.saveAccessToken(token);
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
        let [err, result] = r;
        if (err && err.message === "EXPIRED_TOKEN") {
          return downloadDataset(toDownloadId); // Already cleared the token, now will redirect to auth
        }
      });
    }
  }, [url]);

  return (
    <Styles>
      <Row style={{ height: "100%" }}>
        <Col md={4} className="filters-c">
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
        </Col>
        <Col md={8} className="datasets-c">
          <div
            style={{
              display: "flex",
              justifyContent: "space-between",
              alignItems: "center",
            }}
          >
            <h2 className="datasets-title">Datasets</h2>
            <input
              type="text"
              placeholder="Search datasets..."
              className="dataset-search"
            />
          </div>
          <Row>
            {datasets?.map((i) => (
              <DatasetCard {...i} />
            ))}
          </Row>
        </Col>
      </Row>
    </Styles>
  );
};

export default Datasets;
