import React from 'react';


function Block({ block }) {
    const { timestamp, hash, data } = block;
    const hashDisplay = `${hash.substring(0,15)}...`;
    const timestampDisplay = new Date(timestamp).toLocaleString();
    const dataDisplay = 

}

export default Block;