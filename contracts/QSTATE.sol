// 1. IDENTITAS LISENSI
// SPDX-License-Identifier: MIT

// 2. VERSI BAHASA
pragma solidity ^0.8.20;

// 3. IMPORT STANDAR DUNIA
import "@openzeppelin/contracts/token/ERC20/ERC20.sol";

// 4. DEKLARASI KONTRAK & PEWARISAN
contract QuorumStateCoin is ERC20 {

    // 5. INSIALISASI (AKTA KELAHIRAN)
    constructor() ERC20("Quorum State", "QSTATE") {

        // 6. PROSES MINTING (PENCETAKAN UANG)
        _mint(msg.sender, 1000000000000 * 10 ** decimals());
    }
}
