import { FILTER_ROUTES } from "../constants/Routes";

export const listDataTypes = async () => {
  let result = await fetch(FILTER_ROUTES.LIST_DATA_TYPES, {
    method: "GET",
    url: FILTER_ROUTES.LIST_DATA_TYPES,
    headers: {
      Accept: "application/json",
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

export const listAnnotations = async () => {
  let result = await fetch(FILTER_ROUTES.LIST_ANNOTATIONS, {
    method: "GET",
    url: FILTER_ROUTES.LIST_ANNOTATIONS,
    headers: {
      Accept: "application/json",
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

export const listSources = async () => {
  let result = await fetch(FILTER_ROUTES.LIST_SOURCES, {
    method: "GET",
    url: FILTER_ROUTES.LIST_SOURCES,
    headers: {
      Accept: "application/json",
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

export const listFormats = async () => {
  let result = await fetch(FILTER_ROUTES.LIST_FORMATS, {
    method: "GET",
    url: FILTER_ROUTES.LIST_FORMATS,
    headers: {
      Accept: "application/json",
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

export const listCompressions = async () => {
  let result = await fetch(FILTER_ROUTES.LIST_COMPRESSIONS, {
    method: "GET",
    url: FILTER_ROUTES.LIST_COMPRESSIONS,
    headers: {
      Accept: "application/json",
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

export const listTypes = async () => {
  let result = await fetch(FILTER_ROUTES.LIST_TYPES, {
    method: "GET",
    url: FILTER_ROUTES.LIST_TYPES,
    headers: {
      Accept: "application/json",
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

export const listLicenses = async () => {
  let result = await fetch(FILTER_ROUTES.LIST_LICENSES, {
    method: "GET",
    url: FILTER_ROUTES.LIST_LICENSES,
    headers: {
      Accept: "application/json",
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
