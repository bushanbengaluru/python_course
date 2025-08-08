# go to Empcard.js
import './EmpCard.css';
function EmpCard(pros) # props is a object
{
    return(
        <div className="empcardcomp">
            <p>Name:{pros.name}</p>
            <p>Age:{pros.age}</p>
            <p>Gender:{pros.gender}</p>
        </div>
    )
}
export default EmpCard;
# now go to Main.js
return(
        <div className="maincomp">
        {Person.map((obj)=>{
            return <EmpCard name={obj.name} age={obj.age} gender={obj.gender}/>
        })}
        </div>
# now change the box space
      # go to EmpCard.css
    empcardcomp{
    width: 150px;
    height: 150px;
    border: 2px solid black;
    float: left;
    margin-left: 5px;
    margin-top: 10px;
   
}
# now we want no of data so go to main.js
copy paste some same record like
      ,{
        name:'Hanuma',
        age:30,
        gender:"M"
    },{
        name:'Hanuma',
        age:30,
        gender:"M"
    },{
        name:'Hanuma',
        age:30,
        gender:"M"
    }
        
# here react js divider int small small re-usable components
# in EmpCard.js
        function EmpCard({name,age,gender}) // we can change the like also
{
    return(
        <div className="empcardcomp">
            <p>Name:{name}</p>
            <p>Age:{age}</p>
            <p>Gender:{gender}</p>
        </div>







        
