import React from 'react';
import Plot from 'react-plotly.js';

const DashboardForm = ({ id }) => {
  const barVerticalData = {
    x: ['A', 'B', 'C', 'D', 'E'],
    y: [4, 2, 5, 8, 3],
    type: 'bar',
    name: 'Bar Vertical',
    marker: {
      color: 'blue', // Cor das barras verticais
      width: 2
    },
  };

  const barLayout = {
    width: 400,
    height: 400,
    margin: { l: 50, r: 50, t: 50, b: 50 },
    xaxis: {
      showline: true,
      linewidth: 2,
      linecolor: 'white',
      gridcolor: '#aaa',
    },
    yaxis: {
      showline: true,
      linewidth: 2,
      linecolor: 'yellow',
      gridcolor: '#aaa',
    },
    title: 'Bar Vertical Chart',
    plot_bgcolor: '#333',
    paper_bgcolor: '#555',
    font: {
      family: 'Arial, sans-serif',
      size: 16,
      color: 'white',
      bold: true,
      italics: false,
      underline: false,
      opacity: 1,
    },
  };

  return (
    <div>
      <Plot data={[barVerticalData]} layout={barLayout} />
    </div>
  );
};

export default DashboardForm;