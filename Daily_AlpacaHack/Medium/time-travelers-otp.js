import crypto from "node:crypto";

// index.js からコピーしたロジック
const digits = 6;
const timeStep = 30;

function hotp(key, counter) {
    const buf = Buffer.alloc(8);
    buf.writeUInt32BE((counter & 0xffff_ffff_0000_0000) >>> 32, 0);
    buf.writeUInt32BE(counter & 0x0000_0000_ffff_ffff, 4);
    return truncate(hmac_sha_1(key, buf));
}

function hmac_sha_1(key, buf) {
    const hmac = crypto.createHmac("sha1", key);
    return hmac.update(buf).digest();
}

function truncate(hash) {
    const offset = (hash[19] || 0) & 0x0f;
    const value = hash.readUint32BE(offset) & 0x7fffffff;
    return value % 10 ** digits;
}

function decodeBase32(str) {
    const alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ234567";
    let bits = "";
    for (const char of str) {
        const idx = alphabet.indexOf(char.toUpperCase());
        bits += idx.toString(2).padStart(5, "0");
    }
    const bytes = [];
    for (let i = 0; i + 8 <= bits.length; i += 8) {
        bytes.push(parseInt(bits.slice(i, i + 8), 2));
    }
    return Buffer.from(bytes);
}

// 1. 現代のページからシークレットを入手
const secretBase32 = "MQJZZVVPER3OXQ432ZS2LHPAEPHWWKAA";
const secret = decodeBase32(secretBase32);

// 2. 「未来のサーバーの時間」を算出する
// 現代のUnix時間 + faketime で進められた秒数
const offsetSeconds = 128849018790;
const futureUnixTimeSeconds = Math.floor(Date.now() / 1000) + offsetSeconds;

// 3. 未来のカウンター値から TOTP を計算
const counter = Math.floor(futureUnixTimeSeconds / timeStep);
const futureCode = hotp(secret, counter).toString().padStart(digits, "0");

// 4. 未来の TOTP を出力、これを30秒以内に未来のページに入力する
console.log(`[+] Future TOTP Code: ${futureCode}`);