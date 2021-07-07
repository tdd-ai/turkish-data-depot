import styled from "styled-components";

const DataSetCardsContainer = styled.div`
  display: grid;
  grid-template-columns: repeat(2, minmax(0, 1fr));
  column-gap: 16px;
`;

const DatasetsContainer = styled.div`
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
    margin-bottom: 16px;
    padding: 12px;
    border-radius: 12px;
    background: #f3f3f3;
    cursor: pointer;
    width: 100%;

    transition: background 0.3s ease;

    &:hover {
      background: #e0e0e0;
    }
  }

  .datasets-c {
    width: 70%;
    height: 100%;
    border-left: 1px solid #bec0c2;
  }

  .datasets-title {
    margin-bottom: 0px;
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
    font-weight: 500;
    line-height: 1.2;
    background-color: rgba(248, 151, 28, 0.3);
    color: rgba(156, 87, 0);

    &:hover {
      background-color: rgba(248, 151, 28);
      color: white;
    }
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
    font-size: 16px;
    height: 20px;
    border-radius: 8px;
    border: 1px solid #bec0c2;
    padding: 16px 8px;

    &:focus {
      outline: none !important;
      border-color: #009dd2;
    }
  }

  .download-button {
    display: flex;
    align-items: center;
    justify-content: center;

    padding: 5px 10px;
    margin-top: 8px;

    border: none;
    border-radius: 8px;

    cursor: pointer;
    font-size: 12px;
    line-height: 1.2;

    background-color: #a6e9ff;
    color: #009dd2;

    font-weight: 500;
    width: fit-content;
  }
`;

export { DatasetsContainer, DataSetCardsContainer };
