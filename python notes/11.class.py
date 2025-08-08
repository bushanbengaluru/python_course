# get the data to owr django application in react js
# in owr API code we do some configaration that is corsheader(cross orijen resource sharing)
# cadheader : access you application to another application
# now go to owr django project
# now open in vs code
# now first install corshearders
# pip install django-cors-headers
# next go to settings.py
# and INSTALLED_APPS
  'corsheaders',
 'debug_toolbar',
 # and to go MIDDLEWARE
   'debug_toolbar.middleware.DebugToolbarMiddleware',
    #'firstapp.middleware.MyMidleware',
   'corsheaders.middleware.CorsMiddleware',
based that middlewarae we get wich application data we get
  that is allow
# in setting.py last
 # cros headers
CORS_ALLOW_ALL_ORIGINS=True #
# now run the server
python manage.py runserver

# and then go to API app
 in  urls.py
  path('getemployees/',views.getemployeesapi),

# now open another vs code and take ur react application
# first install the axios in react js 

 axios: based on that we can get api data
 npm install axios
# creatae GetEmployees.js
import axios from "axios";
import { useEffect } from "react";

function GetEmployees(){
    useEffect(()=>{
       axios.get('http://127.0.0.1:8000/api/getemployees/').then(
     (resp)=>{
        console.log(resp);
        console.log(resp.data);
     }
       ).catch((err)=>{ // in case get any error
        console.log(err)
       })
       // axios get calling retunrs promis
       //in then we have a methond that is respoce
    },[])
    return(
        <div>Calling get api in django</div>
    )
}
export default GetEmployees;
#and go to Main.js
render GetEmployee.js file
import GetEmployees from "./GetEmployees";
function Main(){
    
    return(
        <div className="maincomp">
         <GetEmployees />
        </div>

    );
}
export default Main;
# then run react app
npm start and go to inspect check api data
# now i want this data in to page so re-rendering the data
 by using useState
 import axios from "axios";
import { useEffect } from "react";
import { useState } from "react";
function GetEmployees(){
     let[data,setData]=useState([]);
    useEffect(()=>{
       axios.get('http://127.0.0.1:8000/api/getemployees/').then(
     (resp)=>{
        console.log(resp);
        #console.log(resp.data);
        setData(resp.data)
     }
       ).catch((err)=>{ // in case get any error
        console.log(err)
       })
       // axios get calling retunrs promis
       //in then we have a methond that is respoce
    },[])
    return(
        <div>
            <h1>Calling get api in django</h1>
           {data.map((obj)=>{
            return <p>{obj.eid}-{obj.ename}-{obj.sal}</p>
           })}
        </div>
    )
}
export default GetEmployees;
# now go to EmpCard.js
change the colunm name based on owr colunm
function EmpCard(props) // props is a object
{
    return(
        <div className="empcardcomp">
          <p>Eid:{props.eid}</p>
            <p>Name:{props.ename}</p>
            
            <p>sal:{props.sal}</p>
        </div>
    )
}
# and go to Main.css
.maincomp p{
    #display: inline; remove this
    margin-right: 20px;
}
#now go to GetEmployees.js
import EmpCard from "./EmpCard";
       return(
        <div>
            <h1>Calling get api in django</h1>
           {data.map((obj)=>{
            //return <p>{obj.eid}-{obj.ename}-{obj.sal}</p>
           return <EmpCard eid={obj.eid} ename={obj.ename} sal={obj.sal}/>
           })}
        </div>






 






















