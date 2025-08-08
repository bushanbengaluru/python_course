# in UpdateEmployees.js file
import axios from "axios";
import { useState } from "react";

function UpdateEmployess(){
    let [eid,setEid]=useState(0);
    let [data,setdata]=useState({})#// we can get object data
    let getdata=()=>{
        let fetch_url='http://127.0.0.1:8000/api/modify/'+eid+'/';
        axios.get(fetch_url).then((resp)=>{
            console.log(resp);
            console.log(resp.data);
            setdata(resp.data);# add this 
        })
        }
    return(
        <div className="updateempcomp">
          <label>
            Employee No:
            <input type="text" onChange={(event)=>setEid(event.target.value)}/>
          </label><br/>
          <button onClick={getdata}>Get Data</button>
          // now we can use useState so im calling another component
        </div>
    );
}
export default UpdateEmployess;
# now create another component that is PutComponent.js

function PutComponent(props){
    return(
        <div>

        </div>
    );
}
export default PutComponent;
# now PutComponent render to UpdateEmployees.js
import PutComponent from "./PutComponent";
<button onClick={getdata}>Get Data</button>
{data ? <PutComponent data={data} />:''}

# now i want the record in text box except eid
import {  useRef } from "react";

function PutComponent({data}){
    let enameRef=useRef();
    let salRef=useRef();
    useEffect(()=>{
       enameRef.current.value=data.ename;
       salRef.current.value=data.sal
       
    },[data]);
   
    return(
        <div className="putempcomp">
            <p>eid:{props.eid}</p>
            <label>
                ename:
                <input ref={enameRef} type="text" />
            </label><br/>
            <label>
                sal:
                <input ref={salRef} type="text" />
            </label><br/>
            <button>upadate</button>
        </div>
    );
}
export default PutComponent;

# now click update button
import axios from "axios";
import {  useEffect, useRef, useState } from "react";
function PutComponent({data}){
    let enameRef=useRef();
    let salRef=useRef();
    let [msg,setMsg]=useState('');
    useEffect(()=>{
       enameRef.current.value=data.ename;
       salRef.current.value=data.sal
       
    },[data]);
    let updatedata=()=>{
        let input_data={
        "eid":data.eid,
        "ename":enameRef.current.value,
        "sal":salRef.current.value
        }
       let put_url='http://127.0.0.1:8000/api/modify/'+data.eid+'/';
        axios.put(put_url,input_data).then((resp)=>{
            if(resp.status === 200)
                setMsg('updated successfully..');
        }).catch((err)=>{
            setMsg('fail to update the data');
        })

    }   
    return(
        <div className="putempcomp">
           
            <label>
                ename:
                <input ref={enameRef} type="text" />
            </label><br/>
            <label>
                sal:
                <input ref={salRef} type="text" />
            </label>
            
            <button onClick={updatedata}>upadate</button>
            <p>{msg}</p>
        </div>
    );
}
export default PutComponent;

