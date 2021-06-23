import { DATASET_ROUTES } from "../constants/Routes";

export const downloadDataset = async () => {
  let result = await fetch(DATASET_ROUTES.DOWNLOAD, {
    method: "POST",
    url: DATASET_ROUTES.DOWNLOAD,
    headers: {
      Accept: "application/json",
      Authorization: localStorage.getItem("token"),
    },
  });
  let status = result.status;
  if (status >= 400) {
    let resText = await result.text();
    throw resText;
  }
  let resJson = await result.json();
  return resJson;
};
