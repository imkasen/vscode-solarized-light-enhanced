"use strict";

import * as fs from "fs";
import { resolve as pathResolve } from "path";

// ----------------------------------------------------------------------------
// 1. Primitive Literals & Variables
// ----------------------------------------------------------------------------
var varLegacy = "Old school";
let letModern = "Single quoted string";
const CONST_UPPER = true;
const isNull = null;
const isUndefined = undefined;

// Numbers
const integer = 42;
const float = 3.14159;
const scientific = 1e4;
const hex = 0xff_00_c0; // Hex with separators
const binary = 0b1010_0001; // Binary
const octal = 0o744; // Octal
const bigInt = 9007199254740991n; // BigInt

// Strings & Templates
const escaped = 'Line 1\nLine 2\tTabbed "Quote"';
const dynamicVal = "dynamic";
const templateLiteral = `String with ${dynamicVal} interpolation`;
const taggedTemplate = html`<div>${templateLiteral}</div>`; // Tagged template

// ----------------------------------------------------------------------------
// 2. Regular Expressions
// ----------------------------------------------------------------------------
const regexLiteral = /^[a-z0-9]+$/i;
const regexObject = new RegExp("ab+c", "gm");
// Named capture groups & lookbehind
const complexRegex = /(?<year>\d{4})-(?<month>\d{2})-(?<day>\d{2})(?<=date)/;

// ----------------------------------------------------------------------------
// 3. Objects, Arrays & Destructuring
// ----------------------------------------------------------------------------
const symbolKey = Symbol("unique");

const settings = {
  id: 1,
  [symbolKey]: "Hidden", // Computed property
  isEnabled: true,
  calculate() {
    // Method shorthand
    return this.id * 2;
  },
  // Spread operator
  ...{ nested: true },
};

// Destructuring with renaming and default values
const { id: userId, isEnabled = false } = settings;
const [firstItem, ...restItems] = [1, 2, 3, 4];

// ----------------------------------------------------------------------------
// 4. Operators & Control Flow
// ----------------------------------------------------------------------------
const a = 5,
  b = 10;
let result = 0;

// Arithmetic & Bitwise
result = ((a + b) * (b - a)) / 2;
result = (a << 2) | ((b & 1) ^ ~a);

// Logical Assignment (ES2021)
let x = null;
x ??= "default"; // Nullish coalescing assignment
x ||= "fallback"; // OR assignment
x &&= "modify"; // AND assignment

// Ternary & Nullish Coalescing
const status = a > b ? "Active" : "Inactive";
const value = x ?? "Nullish Fallback";

// Optional Chaining
const street = settings?.address?.street;

// Control Structures
try {
  if (a !== b && b >= 10) {
    throw new Error("Validation failed");
  } else if (a === 0) {
    // do nothing
  } else {
    switch (status) {
      case "Active":
        break;
      default:
        console.log("Unknown");
    }
  }
} catch (err) {
  console.error(err);
} finally {
  // Loop labels
  outerLoop: for (let i = 0; i < 5; i++) {
    while (result > 0) {
      result--;
      if (result === 2) continue outerLoop;
    }
  }
}

// ----------------------------------------------------------------------------
// 5. Functions (Arrow, Generator, Async)
// ----------------------------------------------------------------------------

// Function Declaration
function legacyFunc(p1, p2) {
  return arguments.length;
}

// Arrow Function (Implicit return)
const arrowAdd = (a, b) => a + b;

// Async Arrow with Block
const fetchData = async (url) => {
  try {
    const resp = await fetch(url);
    return await resp.json();
  } catch {
    return null;
  }
};

// Generator Function
function* idGenerator() {
  let id = 0;
  while (true) yield ++id;
}

// ----------------------------------------------------------------------------
// 6. Classes (ES6+ and Modern Features)
// ----------------------------------------------------------------------------

class User {
  // Static Fields
  static MAX_USERS = 1000;
  static #internalCount = 0; // Private static

  // Public Field
  role = "guest";

  // Private Field
  #passwordHash;

  constructor(username, password) {
    this.username = username;
    this.#passwordHash = this.#encrypt(password);
    User.#internalCount++;
  }

  // Getter & Setter
  get password() {
    return "********";
  }
  set password(val) {
    this.#passwordHash = this.#encrypt(val);
  }

  // Private Method
  #encrypt(str) {
    return str.split("").reverse().join("");
  }

  // Static Block (ES2022)
  static {
    console.log("User class loaded");
  }

  login() {
    console.log(`${this.username} logged in.`);
  }
}

// Inheritance
class Admin extends User {
  constructor(name, pass) {
    super(name, pass);
    this.role = "admin";
    // Super access
    super.login();
  }
}
