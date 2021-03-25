import { useState } from "react";
import styled from "styled-components";
import Types from "../data/type.filter.json";
import DataTypes from "../data/data-type.filter.json";
import Annotation from "../data/annotation.filter.json";
import Source from "../data/source.filter.json";
import Compression from "../data/compression.filter.json";
import License from "../data/license.filter.json";
import Tooltip from "react-bootstrap/Tooltip";
import OverlayTrigger from "react-bootstrap/OverlayTrigger";
import DummyData from "../data/dummy_data.json";
import Row from "react-bootstrap/Row";
import Col from "react-bootstrap/Col";

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
`;

const Filters = ({ title, filters }) => {
  const [isExpanded, setExpanded] = useState(false);
  let keys = Object.keys(filters);
  const sliceSize = 4;

  return (
    <>
      <span style={{ fontWeight: 500, marginBottom: 10 }}>{title}</span>
      <div style={{ marginBottom: 20, width: "100%" }} className="tags-c">
        {(isExpanded ? keys : keys.slice(0, sliceSize)).map((el) => {
          const renderTooltip = (props) => (
            <Tooltip id="button-tooltip" {...props}>
              {filters[el]}
            </Tooltip>
          );
          return (
            <OverlayTrigger
              placement="top"
              // delay={{ show: 250, hide: 400 }}
              overlay={renderTooltip}
            >
              <div className="filter">{el}</div>
            </OverlayTrigger>
          );
        })}
        {keys.length - sliceSize > 0 && (
          <div onClick={() => setExpanded(!isExpanded)} className="expand">
            {isExpanded ? "⇠" : keys.length - sliceSize + " more"}
          </div>
        )}
      </div>
    </>
  );
};

const DatasetCard = ({ catalog, name, description }) => {
  return (
    <Col md={5} className="datasetcard">
      <div className="dataset-name">{name}</div>
      <h3>{catalog}</h3>
      <div className="dataset-desc">{description}</div>
    </Col>
  );
};

const Datasets = () => {
  return (
    <Styles>
      <Row style={{ height: "100%" }}>
        <Col md={4} className="filters-c">
          <h2 className="datasets-title">Filters</h2>
          <Filters title="Type" filters={Types} />
          <Filters title="Data Types" filters={DataTypes} />
          <Filters title="Annotation" filters={Annotation} />
          <Filters title="Source" filters={Source} />
          <Filters title="Compression Type" filters={Compression} />
          <Filters title="License" filters={License} />
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
            {DummyData.map((i) => (
              <DatasetCard {...i} />
            ))}
          </Row>
        </Col>
      </Row>
    </Styles>
  );
};

export default Datasets;
