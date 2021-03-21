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

const Styles = styled.div`
  display: flex;
  flex-direction: row;
  height: 100vh;
  .filters-c {
    display: flex;
    width: 30%;
    height: 100%;
    padding: 20px 40px;
    flex-direction: column;
  }
  .datasets-c {
    width: 70%;
    height: 100%;
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
    background-color: rgba(77, 199, 239, 0.5);
    &:hover {
      background-color: rgba(77, 199, 239, 0.8);
    }
    color: #063747;
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
  }
`;

const Filters = ({ title, filters }) => {
  const [isExpanded, setExpanded] = useState(false);
  let keys = Object.keys(filters);
  const sliceSize = 4;

  return (
    <>
      <span style={{ fontWeight: 500 }}>{title}</span>
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
            {isExpanded ? "⇠" : "+" + (keys.length - sliceSize)}
          </div>
        )}
      </div>
    </>
  );
};

const Datasets = () => {
  return (
    <Styles>
      <div className="filters-c">
        <Filters title="Type" filters={Types} />
        <Filters title="Data Types" filters={DataTypes} />
        <Filters title="Annotation" filters={Annotation} />
        <Filters title="Source" filters={Source} />
        <Filters title="Compression Type" filters={Compression} />
        <Filters title="License" filters={License} />
      </div>
      <div className="datasets-c"></div>
    </Styles>
  );
};

export default Datasets;
