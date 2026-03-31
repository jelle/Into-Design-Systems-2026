# Product Primitives - The New Material of Design Systems
**Speaker**: Jacenia (design systems leader, formerly Shopify Polaris)
**Conference**: Into Design Systems AI Conference 2026

## Key Ideas

1. **Today's UI is a middle ground nobody loves** — Forms force new users into premature precision while frustrating power users who need speed; everyone gets a subpar experience because adapting at scale was impossible.

2. **Intent-based UI is the shift** — Instead of navigating to pages and filling fields, users state a goal and AI composes the right surface for that specific intent, context, and scale.

3. **AI is already doing this today** — Claude, for example, detects recipe intent and returns a recipe card with a timer; it detects ranking intent and returns a sortable list. The pattern is live and working.

4. **Product primitives are the new design material** — Objects users create and manipulate (discount, order, task, event) need the same design rigor we currently give buttons and dropdowns: anatomy, lifecycle states, relationships, visual signifiers.

5. **Surfaces replace static page layouts** — A surface is a context-aware container that adapts a primitive's presentation to match user intent (e.g., canvas for exploration, batch for bulk edits, confirmation for reviewing changes).

6. **Visual signifiers are critical and underinvested** — Every primitive needs a glanceable identity so users recognize it wherever it appears across surfaces — not just on its "home" page.

7. **Relationships are invisible in today's flat navigation** — Objects like collections and products sit at the same nav level even though they have clear hierarchy; intent-driven UI is an opportunity to visualize these relationships properly.

8. **AI without primitive context defaults to page layouts** — A demo with Claude Code + Polaris showed that without primitive/surface specs, AI always falls back to the same resource-detail page layout regardless of task. With context, it composed appropriate surfaces and invented a new bulk date-picker control.

9. **Context shapes AI reasoning, not just output** — With primitive context, Claude narrated strategic decisions ("this is a batch intent, I'll build a batch surface") rather than just listing components. Better context = better thinking.

10. **Design system teams become architects, not builders** — The DS team defines the grammar (surface types, interaction logic, composition patterns, visual signifier system). Domain teams supply the vocabulary (their specific fields, rules, states, and relationships).

11. **Start small: identify your core primitives first** — Every product has 3-5 objects that define what it is. Map their relationships, establish visual signifiers, find where flat navigation is failing users — that's your starting point.

12. **The intent signal is the missing layer** — AI needs explicit signals (account age, first visit, message structure, scope of change) mapped to surfaces to know what to compose. This documentation doesn't exist yet and needs to be built.

13. **The precursor is a mindset shift from pages to portable objects** — Shopify started by treating discounts as portable objects that could appear in intent modals on any page, before wiring anything to AI. That thinking shift is the real first step.
