import { useState } from "react";

import Tooltip from "react-bootstrap/Tooltip";
import OverlayTrigger from "react-bootstrap/OverlayTrigger";

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

export default Filters;
