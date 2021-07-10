const StorageKeys = {
  accessToken: "accessToken",
  refreshToken: "refreshToken",
};

const saveAccessToken = (accessToken) => {
  localStorage.setItem(StorageKeys.accessToken, accessToken);
};

const saveRefreshToken = (refreshToken) => {
  localStorage.setItem(StorageKeys.refreshToken, refreshToken);
};

const getAccessToken = () => {
  return localStorage.getItem(StorageKeys.accessToken);
};

const getRefreshToken = () => {
  return localStorage.getItem(StorageKeys.refreshToken);
};

const removeItem = (key) => {
  return localStorage.removeItem(key);
};

const StorageService = {
  StorageKeys,
  saveAccessToken,
  saveRefreshToken,
  getAccessToken,
  getRefreshToken,
  removeItem,
};

export default StorageService;
