// Structure of linked list Node
/* typedef struct Node {
    int data;
    struct Node* next;
} Node; */

// Function to create a new node
/* Node* createNode(int val) {
    Node* node = (Node*)malloc(sizeof(Node));
    node->data = val;
    node->next = NULL;
    return node;
} */

typedef struct {
    // Initialize your data members
    Node *top;
    int currSize;
} myStack;

// Initialize stack
void initStack(myStack* s) {
    s->top = NULL;
    s->currSize = 0;
}

bool isEmpty(myStack* s) {
    // Check if stack is empty
    return s->top==NULL;
}

void push(myStack* s, int x) {
    // Adds an element to the top of the stack
    Node *temp=createNode(x);
    temp->next=s->top;
    s->top=temp;
    s->currSize++;
}

void pop(myStack* s) {
    // Removes an element from the top of the stack
    if(isEmpty(s)){
        return;
    }
    Node *curr=s->top;
    s->top=s->top->next;
    free(curr);
    s->currSize--;
}

int peek(myStack* s) {
    // Returns the top element of the stack
    // If the stack is empty, return -1
    if(isEmpty(s)){
        return -1;
    }
    return s->top->data;
}

int size(myStack* s) {
    // Returns the current size of the stack
    return s->currSize;
}

// Synced seamlessly with LeetHub Pro
// Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
// Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna