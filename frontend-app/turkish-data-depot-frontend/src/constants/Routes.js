const BASE_ADDRESS = "https://data.tdd.ai/api";

export const FILTER_ROUTES = Object.freeze({
  LIST_DATA_TYPES: BASE_ADDRESS + "/enum/data-types/",
  LIST_ANNOTATIONS: BASE_ADDRESS + "/enum/annotations/",
  LIST_SOURCES: BASE_ADDRESS + "/enum/sources/",
  LIST_FORMATS: BASE_ADDRESS + "/enum/formats/",
  LIST_COMPRESSIONS: BASE_ADDRESS + "/enum/compressions/",
  LIST_TYPES: BASE_ADDRESS + "/enum/types/",
  LIST_LICENSES: BASE_ADDRESS + "/enum/licenses/",
  LIST_DATASETS: BASE_ADDRESS + "/datasets",
});

export const DATASET_ROUTES = Object.freeze({
  DOWNLOAD: BASE_ADDRESS + "/files/download/",
});
