import { RestService } from './restService';
import { Injectable } from "@angular/core";


@Injectable()
export class DataManagement {

    constructor(
        private restService: RestService,
    ) {

    }

    //public login()

    public logout(): Promise<any> {
        return new Promise((resolve, reject) => {
            return this.restService.logout().then((data) => {
                resolve(data);
            }).catch((error) => {
                reject('error');
            });
        });
    }

}