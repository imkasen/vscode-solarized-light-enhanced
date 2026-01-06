// ----------------------------------------------------------------------------
// 1. Basic Types, Enums & Tuples
// ----------------------------------------------------------------------------

// Enums (often have specific colors)
enum Direction {
  Up = 1,
  Down,
  Left = "LEFT", // String enum
  Right = "RIGHT",
}

const enum ConstColors {
  Red = 0xff0000,
  Green = 0x00ff00,
  Blue = 0x0000ff,
}

// Primitives & Tuples
let isDone: boolean = false;
let lines: number = 42;
let nameStr: string = "TypeScript";
let tuple: [string, number] = ["hello", 10]; // Tuple
let unionType: string | number | null = "maybe"; // Union type separator

// ----------------------------------------------------------------------------
// 2. Interfaces & Type Aliases
// ----------------------------------------------------------------------------

type UUID = string;

interface IIdentifiable {
  readonly id: UUID; // Readonly modifier
  optional?: string; // Optional modifier
}

// Intersection Type
interface ILoggable {
  log(): void;
}

// Extending Interfaces
interface UserSettings extends IIdentifiable, ILoggable {
  theme: "dark" | "light"; // Literal type
  [key: string]: any; // Index signature
  metadata: unknown; // Unknown type
}

// ----------------------------------------------------------------------------
// 3. Classes & Access Modifiers
// ----------------------------------------------------------------------------

abstract class BaseService {
  abstract start(): void;
  protected stop(): void {
    console.log("Stopped");
  }
}

// Decorator usage (Experimental/Stage 3)
@frozen
class UserService extends BaseService implements IIdentifiable {
  // Parameter properties (public/private in constructor)
  constructor(public readonly id: UUID, private _dbConnection: any) {
    super();
  }

  // Static properties with access modifiers
  public static instanceCount: number = 0;

  // Method with specific return type
  public override start(): void {
    // 'override' keyword
    this.log();
  }

  public log(): void {
    console.log(`User ${this.id}`);
  }

  // Assertions
  public getData(): string {
    return (this._dbConnection as any).data!; // 'as' and Non-null assertion '!'
  }
}

function frozen(constructor: Function) {
  Object.freeze(constructor);
  Object.freeze(constructor.prototype);
}

// ----------------------------------------------------------------------------
// 4. Generics (The ultimate highlighter test)
// ----------------------------------------------------------------------------

// Generic Interface
interface ResponseData<T = any> {
  status: number;
  data: T;
  error?: string;
}

// Generic Function with Constraints
function getProperty<T, K extends keyof T>(obj: T, key: K) {
  return obj[key];
}

const userRes: ResponseData<string> = {
  status: 200,
  data: "Success",
};

// ----------------------------------------------------------------------------
// 5. Functions & Overloads
// ----------------------------------------------------------------------------

// Function Overloads
function padding(all: number): object;
function padding(topAndBottom: number, leftAndRight: number): object;
function padding(a: number, b?: number): object {
  if (b === undefined) return { top: a, bottom: a, left: a, right: a };
  return { top: a, bottom: a, left: b, right: b };
}

// 'this' parameter typing
function handleClick(this: HTMLElement, e: Event) {
  this.innerHTML = "Clicked";
}

// ----------------------------------------------------------------------------
// 6. Advanced Type Features (Type Gymnastics)
// ----------------------------------------------------------------------------

// Mapped Types
type Readonly<T> = {
  readonly [P in keyof T]: T[P];
};

// Conditional Types
type TypeName<T> = T extends string ? "string" : T extends number ? "number" : T extends boolean ? "boolean" : "object";

// Template Literal Types
type EventName = "click" | "scroll" | "mousemove";
type EventHandler = `on${Capitalize<EventName>}`; // "onClick" | "onScroll"...

// Utility usage
type PartialUser = Partial<UserSettings>;

// ----------------------------------------------------------------------------
// 7. Modern TS Features (Satisfies, Assertions)
// ----------------------------------------------------------------------------

// 'satisfies' operator (TS 4.9+)
const myPalette = {
  red: [255, 0, 0],
  green: "#00ff00",
} satisfies Record<string, string | number[]>;

// 'const' assertions
const config = {
  endpoint: "https://api.example.com",
  retries: 3,
} as const;

// Type Guards
function isString(test: any): test is string {
  return typeof test === "string";
}

if (isString(unionType)) {
  console.log(unionType.toUpperCase()); // TS knows it's a string here
}

export { UserService, Direction, type IIdentifiable };
