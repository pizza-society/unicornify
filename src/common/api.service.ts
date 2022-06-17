// import axios, { AxiosInstance } from "axios";
import http from "@/http-common";
class ApiService {
   get(resource: any): Promise < any > {
      return http.get(`${resource}/`).catch((error) => {
         throw error;
      });
   }
   customGetOne(resource: any, id: any, customEndpoint: any): Promise < any > {
      return http.get(`${resource}/${id}/${customEndpoint}/`).catch((error) => {
         throw error;
      });
   }
   post(resource: any, params: any): Promise < any > {
      return http.post(`${resource}/`, params).catch((error) => {
         // console.log(error)
         throw error;
      });
   }
   customPost(resource: any, customEndpoint: any, payload: any): Promise < any > {
      return http
         .post(`${resource}/${customEndpoint}/`, payload)
         .catch((error) => {
            throw error;
         });
   }
   activate(resource: any, slug: any): Promise < any > {
      return http.get(`${resource}/${slug}/activate/`).catch((error) => {
         throw error;
      });
   }

   deactivate(resource: any, slug: any): Promise < any > {
      return http.get(`${resource}/${slug}/deactivate/`).catch((error) => {
         throw error;
      });
   }

   uploadFile(resource: any, body: any): Promise < any > {
      return http.post(`${resource}/`, body).catch((error) => {
         throw error;
      });
   }
}
export default new ApiService();