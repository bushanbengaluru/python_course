# now run the django application and react applications
#now till now we are getting the data
# now i want post the data
# now create PostEmployees.js
function PostEmployees(){
    return(
      <div className="postcomp">
        <label>
            Employee No :
            <input type="text" />
        </label><br/>
         <label>
         Employee Name:
         <input type="text" />
     </label><br/>
      <label>
      Employee sal:
      <input type="text" />
  </label><br/>
  <button>Insert</button>
  </div>
    );
}
export default PostEmployees;
# now go to Main.js
import PostEmployees from "./PostEmployees";
function Main(){  
    return(
        <div className="maincomp">
         <PostEmployees />
        </div>

# now write css for botton
# now create PostEmployee.css
 .postcomp button{
   width: 100px;
   height: 40;
   background-color: blue;
   color: white;
   border: none;
   font-size: large;
   margin-top: 5px;
   margin-left: 100px;
}
      .postcomp p{
    font-size: 20px;
    display: inline-block;
}
# nad go to PostEmployees.js
import './PostEmployees.css';

# now we can post the data in that point of you we can call the useRef

#now in PostEmployees.js
        
import axios from 'axios';
import './PostEmployees.css';
import { useRef } from 'react';
function PostEmployees(){
    let eidRef=useRef(0);
    let enameRef=useRef('');
    let salRef=useRef(0);
    let postdata=()=>{
        let input_data={
            "eid":eidRef.current.value,
            "ename":enameRef.current.value,
            "sal":salRef.current.value,
        }
        axios.post('http://127.0.0.1:8000/api/getemployees/',input_data).then(
            (resp)=>{
                console.log(resp);
            }
        ).catch((err)=>{
            console.log(err);
        })
    }
    return(
        <div className="postcomp">
        <label>
           <p> Employee No </p>
            <input ref={eidRef} type="text" />
        </label><br/>
         <label>
         <p>Employee Name</p>
         <input ref={enameRef} type="text" />
     </label><br/>
      <label>
      <p>Employee sal</p>
      <input ref={salRef} type="text" />
  </label><br/>
  <button onClick={postdata}>Insert</button>
  </div>
    );
}
export default PostEmployees;
# now once we can click the button clear the input
axios.post('http://127.0.0.1:8000/api/getemployees/',input_data).then(
      (resp)=>{
      console.log(resp);
        eidRef.current.value='';
        enameRef.current.value='';
         salRef.current.value='';
            }
        








