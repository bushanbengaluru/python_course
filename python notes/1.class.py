# Reaact Js: react js is a library of javascript
#  it is only take care of presentation part(like UI)
# why react popular : it is a single page application
# when we are learn react js we can understand
# 1 componet :javascript functions
# 2 jsx : html inside javascript
# 3 props
# 4 state

#how to install the packager
npm -- node package manager
# # first go to system create folder in that folder
# npx -- execute the pakcages
npx create-react-app webapp_fronted

#SRC -- is the main folder
 # where we have the all the component we are creating
  App.js --is a main component
  index,js-- main file wich is used to we render the index.html

  package.json -- another importent file we can use
     dependentfy files

now run the file
  # npm start
# go to App.js remove with in the <div className="App"> data
# and then
write owr own

# exm <h1>my project</h1>
# and we can create own component also
go to src -create file-like First.js --
#when we are create component first latter should be upper
1 in First.js

function First(){
    return (
     <div>this first components</div>
    );
}
export default First;

#step 2: then render the main app that is App.js
   go to App.js
   import First from './First';
   function App() {
  return (
    <div className="App">
      <h1>this is my first react project</h1>
      <First />







  

     
