import axios, { AxiosInstance } from "axios";
const apiClient: AxiosInstance = axios.create({
  baseURL: "http://localhost:8080/v1", // Fast Api URL...
  headers: {
    "Content-type": "application/json",
  },
});
export default apiClient;

