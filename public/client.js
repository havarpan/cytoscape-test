/* global cytoscape */

/* jquery:

fetch("/", {
    method: "POST"
  })
    .then(res => res.json())
    .then(response => {
      console.log(JSON.parse(response))
      renderGraph(JSON.parse(response))
    });

*/

// the above without jquery
const getGraph = async function() {
  const data = await fetch("/", {
    method: "POST"
  })
  
  const jsoni = JSON.parse(await data.json())
  console.log(jsoni)
  renderGraph(jsoni)
}
getGraph()


const renderGraph = function(data) {
  
  const cy = cytoscape({
    container: document.getElementById("cy"),
    elements: data,
    style: [
      {
        selector: "node",
        style: {
          label: "data(label)",
          width: "60px",
          height: "60px",
          color: "blue",
          "background-fit": "contain",
          "background-clip": "none"
        }
      },
      {
        selector: "edge",
        style: {
          label: "data(weight)",
          "text-background-color": "yellow",
          "text-background-opacity": 0.4,
          width: "6px",
          "target-arrow-shape": "triangle",
          "control-point-step-size": "140px"
        }
      }
    ],
    layout: {
      name: "cose"
//      name: "circle"
    }
  });
};