import { AnnotationsContainer } from "./DataSetDetails.styled";

const Annotations = ({ annotations }) => {
  return (
    <AnnotationsContainer>
      <h3>Annotations</h3>
      <table>
        <tbody>
          {annotations.map((annotation) => (
            <tr>
              <th>{annotation.name}</th>
              <th>{annotation.description}</th>
            </tr>
          ))}
        </tbody>
      </table>
    </AnnotationsContainer>
  );
};

export default Annotations;
