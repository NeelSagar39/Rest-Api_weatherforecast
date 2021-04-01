import routes from './routes.json';
export default function RouteCleaner(){
    let routeStartandDestination = {}
    Object.keys(routes).forEach((key)=>{
        let routesArray = routes[key]
        if (routesArray.length > 1){
            let routeNumber = routes[key][0]
            let routeStart = routes[key][1]
            let routeEnd = routes[key][routesArray.length-1]
            if (routeNumber === '15'){ 
            console.log(routeStart[0].toString()===routeEnd[0].toString())}
            if (routeStart[0].toString() !== routeEnd[0].toString()){
            let wayPoints = []
            routesArray.forEach((item,index)=>{
                if (index !== 1 && index!== 0 && index !==routesArray.length-1 ){
                    wayPoints.push({
                        location:item.toString(),
                    })
                }
                else{
                    // console.log(routeStart == routeEnd)
                }
            });
            let routeObj = {
                startpoint: routeStart,
                endpoint: routeEnd,
                waypoints: wayPoints,
                routenumber: routeNumber,
            };
            routeStartandDestination[key] = routeObj;           

            }
            else{
                console.log("GG")
            }
    }
})
    const fs = require('fs')
    fs.writeFile('final_routes.json', routeStartandDestination, (err) => {
        if (err) {
            throw err;
        }
        console.log("JSON data is saved.");
    });    
}