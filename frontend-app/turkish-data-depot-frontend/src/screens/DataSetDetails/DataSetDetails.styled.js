import styled from "styled-components";

const AnnotationsContainer = styled.div`
  display: flex;
  flex-direction: column;
  flex: 2;
  padding-right: 16px;
  border-right: 1px solid #e2e2ea;
`;

const ContentContainer = styled.div`
  flex: 1;
  padding: 0 32px;
  border-right: 1px solid #e2e2ea;
  flex: 6;
`;

const DataSetDetailContainer = styled.div`
  font-family: 'Helvetica';
  display: flex;
  flex-direction: row;
  padding: 20px 40px;
  width: 100%;

  blockquote {
    background: #f5f5f5;
    padding: 16px;
    border-left: 8px solid #d2d2d2;
  }

  blockquote p {
    margin-bottom: 0;
  }

  pre {
    white-space: pre-wrap;
  }

  table {
    border-collapse: collapse;
    width: 100%;
  }

  td,
  th {
    font-weight: 500;
    border: 1px solid #e2e2ea;
    text-align: left;
    padding: 8px;
  }

  tr:nth-child(even) {
    background-color: #f3f3f3;
  }

  .download-button {
    display: flex;
    align-items: center;
    justify-content: center;

    width: 100%;
    padding: 12px 16px;
    font-size: 16px;
    font-weight: 500;
    margin-top: 8px;

    border: none;
    border-radius: 8px;

    cursor: pointer;
    line-height: 1.2;

    background-color: #a6e9ff;
    color: #009dd2;

    transition: 0.3s ease;

    &:hover {
      background-color: #a8e1f5;
    }
  }
`;

const FileDetailsContainer = styled.div`
  display: flex;
  flex-direction: column;
  flex: 4;
  padding-left: 16px;
`;

export {
  AnnotationsContainer,
  ContentContainer,
  DataSetDetailContainer,
  FileDetailsContainer,
};
