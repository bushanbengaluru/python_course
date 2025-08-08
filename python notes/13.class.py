# now i want next value
# and previous value
# so i this time i want useRef -- why bcz we can get dirrect values
# now go to GetEmpoyees.js
import axios from "axios";
import { useEffect } from "react";
import { useState } from "react";
import { useRef } from "react";  # import useRef
import EmpCard from "./EmpCard";
function GetEmployees(){
     let[data,setData]=useState([]);
     let nextRef=useRef(''); #-- write this
     let prevRef=useRef(''); # -- write this
    useEffect(()=>{
       axios.get('http://127.0.0.1:8000/api/getemployees/').then(
     (resp)=>{
        console.log(resp);
        console.log(resp.data);
       nextRef.current=resp.data.next; #-- write this
       prevRef.current=resp.data.previous; #--write this
        setData(resp.data.results)
     }
       ).catch((err)=>{ // in case get any error
        console.log(err)
       })
       // axios get calling retunrs promis
       //in then we have a methond that is respoce
    },[])
         # write this code
         let nextdata =()=>{ # write this
        axios.get(nextRef.current).then((resp)=>{ # write this
         nextRef.current=resp.data.next; # write this
         prevRef.current=resp.data.previous; #write this
         setData(resp.data.results) #write this
      })
    }
    return(
        <div>
            <h1>Calling get api in django</h1>
           {data.map((obj)=>{
            //return <p>{obj.eid}-{obj.ename}-{obj.sal}</p>
           return <EmpCard eid={obj.eid} ename={obj.ename} sal={obj.sal}/>
           })}
           <button onClick={nextdata}>Next</button> # create this
        </div>
    )
}
export default GetEmployees;
# now one click next next next once complete we can get null
# now total data will get i want next button disable so how to do
 <button onClick={nextdata} disabled={nextRef.current == null}>Next</button> # create this
# now i want previou value
import axios from "axios";
import { useEffect } from "react";
import { useState,useRef } from "react";
import EmpCard from "./EmpCard";
function GetEmployees(){
     let[data,setData]=useState([]);
     let nextRef=useRef('');
     let prevRef=useRef('');
    useEffect(()=>{
       axios.get('http://127.0.0.1:8000/api/getemployees/').then(
     (resp)=>{
        console.log(resp);
        console.log(resp.data);
        nextRef.current=resp.data.next;
        prevRef.current=resp.data.previous;
        setData(resp.data.results)
     }
       ).catch((err)=>{ // in case get any error
        console.log(err)
       })
       // axios get calling retunrs promis
       //in then we have a methond that is respoce
    },[])
    let nextdata =()=>{
      axios.get(nextRef.current).then((resp)=>{
         nextRef.current=resp.data.next;
         prevRef.current=resp.data.previous;
         setData(resp.data.results)
      })
    }
     # we can write this code
    let previousdata =()=>{
      axios.get(prevRef.current).then((resp)=>{
         nextRef.current=resp.data.next;
         prevRef.current=resp.data.previous;
         setData(resp.data.results)
      })
    }
    return(
        <div>
            <h1>Calling get api in django</h1>
           {data.map((obj)=>{
            //return <p>{obj.eid}-{obj.ename}-{obj.sal}</p>
           return <EmpCard eid={obj.eid} ename={obj.ename} sal={obj.sal}/>
           })}
<button onClick={nextdata} disabled={nextRef.current == null}>Next</button>
<button onClick={previousdata} disabled={prevRef.current==null}>Previous</button>
             # create button
        </div>
    )
}
export default GetEmployees;
# now i want css in button so i want GetEmployees.css now
# now create css and go to GetEmployees.css
 .getempcom button{
    width: 100px;
    height: 40px;
    background-color: blue;
    color: white;
    border: none;
   font-size: large;
   margin-right: 10px;
}
# in GetEmployees.js file

go to
import './GetEmployees.css';
return(
        <div className="getempcom"> # give the css class name
            <h1>Calling get api in django</h1>











