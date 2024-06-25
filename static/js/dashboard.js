document.addEventListener('DOMContentLoaded', function() {
    fetch('/get_data/')
        .then(response => response.json())
        .then(data => {
            createBarChart(data);
            
        });

    function createBarChart(data) {
        const margin = {top: 20, right: 30, bottom: 40, left: 90},
              width = 960 - margin.left - margin.right,
              height = 500 - margin.top - margin.bottom;

        const svg = d3.select("#chart")
            .append("svg")
            .attr("width", width + margin.left + margin.right)
            .attr("height", height + margin.top + margin.bottom)
            .append("g")
            .attr("transform", `translate(${margin.left},${margin.top})`);

        const x = d3.scaleBand()
            .range([0, width])
            .padding(0.1);

        const y = d3.scaleLinear()
            .range([height, 0]);

        x.domain(data.map(d => d.country));
        y.domain([0, d3.max(data, d => d.intensity)]);

        svg.selectAll(".bar")
            .data(data)
            .enter()
            .append("rect")
            .attr("class", "bar")
            .attr("x", d => x(d.country))
            .attr("width", x.bandwidth())
            .attr("y", d => y(d.intensity))
            .attr("height", d => height - y(d.intensity))
            .attr("fill", "steelblue");

        svg.append("g")
            .attr("transform", `translate(0,${height})`)
            .call(d3.axisBottom(x))
            .selectAll("text")
            .attr("transform", "rotate(-45)")
            .style("text-anchor", "end");

        svg.append("g")
            .call(d3.axisLeft(y));
    }
});
