import { useHistory } from "react-router-dom";
import StorageService from "../services/StorageService";
import useQuery from "./useQuery";

const useRedirectedData = () => {
  const query = useQuery();
  const history = useHistory();

  const url = window.location.href;
  const token = (/\?token=([\s\S]*)/.exec(url) || [])[1];

  if (token) {
    StorageService.saveAccessToken(token);
    query.delete("token");
    history.replace({
      search: query.toString(),
    });
  }
};

export default useRedirectedData;
