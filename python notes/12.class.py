useRef: it is  Hook wich is used to in variable value
changed we dont want re-rendering and directly dom element
can access that is useRef
# that means directly access the dom element that is use of
    # useRef
#dom element means: input text values
 now create one component Test.js
 function Test(){
    let readinput=()=>{
        let v1=document.querySelector('#t1').value;
        # this is normaly we can call this
    }
    return(
        <div>
            <input type="text" id="t1" />
            <button onClick={readinput}>Click me</button>
        </div>
    );
}
export default Test;
but based on useRef we can access the input tag value
import { useRef } from "react";
function Test(){
    let dataref=useRef(''); # hear we have current is attribute in this current attribute we have a value
    let readinput=()=>{
        //let v1=document.querySelector('#t1').value;
        let v1=dataref.current.value;
        console.log(v1);
    }
    return(
        <div>
            <input ref={dataref} type="text" />
            <button onClick={readinput}>Click me</button>
        </div>
    );
}
export default Test;
# now go to Main.js
import Test from "./Test";
function Main(){
    return(
        <div className="maincomp">
         <Test />
        </div>

    );
}
export default Main;
# now run test.js and go to inspect and give the input value
# and see in console we can get the value

# now incialy we can give the value in test.js
we can get the rama value in input 
function Test(){
    let dataRef=useRef(''); // hear we have current is attribute in this current attribute we have a value
       dataRef.current.value='sita';
  let readinput=()=>{
        //let v1=document.querySelector('#t1').value;
        let v1=dataRef.current.value;
        console.log(v1);
    }
    return(
# now click the button we can see that value in console
          now in case give the value in input also we can
          see that value also
----------------------------------------------------------
# now i want pagination
#now open another vs code and run owr django project
# now go to Main.js        
import GetEmployees from "./GetEmployees";
import Test from "./Test";
function Main(){
    
    return(
        <div className="maincomp">
         <GetEmployees />
        </div>

    );
}
export default Main;
# now go to django project
# and go to api -- view.py -- go to pagination code
          then copy the class name
class FirstApiView(APIView):
          copy this class name
# nad go to urls in api
path('getemployees/',views.FirstApiView.as_view()),

# and now go to GetEmployees.js
          useEffect(()=>{
       axios.get('http://127.0.0.1:8000/api/getemployees/').then(
     (resp)=>{
        console.log(resp);
        console.log(resp.data);
        setData(resp.data.results)
        # just change hear call results
     }
       ).catch((err)=>{ // in case get any error
        console.log(err)
       })




















 
