const express = require('express');
const axios = require('axios');
const app = express();
const PORT = 3001;

const RPC_URL = "http://localhost:8545";

app.use(express.json());

// 🔎 Endpoint 1: Block Viewer
app.get('/api/block/:number', async (req, res) => {
    try {
        const response = await axios.post(RPC_URL, {
            jsonrpc: "2.0",
            method: "eth_getBlockByNumber",
            params: [req.params.number, true],
            id: 1
        });
        res.json(response.data.result);
    } catch (error) {
        res.status(500).json({ error: "Failed to connect to STG-Chain node interface" });
    }
});

// 🎯 Endpoint 2: Address Lookup
app.get('/api/balance/:address', async (req, res) => {
    try {
        const response = await axios.post(RPC_URL, {
            jsonrpc: "2.0",
            method: "eth_getBalance",
            params: [req.params.address, "latest"],
            id: 1
        });
        res.json({ address: req.params.address, balance: response.data.result });
    } catch (error) {
        res.status(500).json({ error: "Address query trace failed" });
    }
});

app.listen(PORT, () => console.log(`🛰️ STG Explorer Backend serving on port ${PORT}`));
