function getNeuroids(){
				  var x = document.getElementById("numberOfNeuroids").value;
				  console.log(x);
				  return x;
			} //function to capture number of neuroids
function getLayers(){
				  var x = document.getElementById("hiddenLayers").value;
				  console.log(x);
				  return x;
			} //function to capture number of layers 
function getWeights() {
				  var x = document.getElementById("weights").value;
				  var values = [x];
				  console.log(values);
				  return values;

			} //function to capture number weights for hidden layers
function getNeuroidProperties() {
				  
				  var kr = document.getElementById("KrValue").value;
				  var umbr = document.getElementById("umbrValue").value;
				  var beta = document.getElementById("BetaValue").value;
				  var maxcount = document.getElementById("maxcountValue").value;
				  var values = [kr, umbr, beta, maxcount];
				  console.log(values);
				  return values;
			} //function to capture properties of Neuroid