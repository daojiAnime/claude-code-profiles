# Confluence-Macros - Storage-Format

**Pages:** 1

---

## Confluence Support

**URL:** https://confluence.atlassian.com/doc/confluence-storage-format-790796544.html

**Contents:**
        - Versions
- Confluence Storage Format
    - Confluence Markup
    - On this page
    - Related content
    - Still need help?
- Headings
- Text effects
- Text breaks
- Lists

The Atlassian Community is here for you.

This page describes the XHTML-based format that Confluence uses to store the content of pages, page templates, blueprints, blog posts and comments. This information is intended for advanced users who need to interpret and edit the underlying markup of a Confluence page.

We refer to the Confluence storage format as 'XHTML-based'. To be correct, we should call it XML, because the Confluence storage format does not comply with the XHTML definition. In particular, Confluence includes custom elements for macros and more. We're using the term 'XHTML-based' to indicate that there is a large proportion of HTML in the storage format.

You can view the Confluence storage format for a given page by choosing

Headings 4 to 6 are also available and follow the same pattern

Note: Created in the editor using Shift + Return/Enter

For rich content like images, you need to use ac:link-body to wrap the contents.

All links received from the editor will be stored as plain text by default, unless they are detected to contain the limited set of mark up that we allow in link bodies. Here are some examples of markup we support in link bodies.

The markup tags permitted within the <ac:link-body> are <b>, <strong>, <em>, <i>, <code>, <tt>, <sub>, <sup>, <br> and <span>.

Supported image attributes (some of these attributes mirror the equivalent HTML 4 IMG element):

Confluence supports page layouts directly, as an alternative to macro-based layouts (using, for example, the section and column macros). This section documents the storage format XML created when these layouts are used in a page.

Indicates that the page has a layout. It should be the top level element in the page.

Represents a row in the layout. It must be directly within the ac:layout tag. The type of the section indicates the appropriate number of cells and their relative widths.

The recognized values of ac:type for ac:layout-section are:

Expected number of cells

The following example shows one of the more complicated layouts from the old format built in the new. The word {content} indicates where further XHTML or Confluence storage format block content would be entered, such as <p> or <table> tags.

Resource identifiers are used to describe "links" or "references" to resources in the storage format. Examples of resources include pages, blog posts, comments, shortcuts, images and so forth.

This screenshot shows a simple template:

The template contains the following variables:

The XML export produces the following code for the template:

Instructional text allows you to include information on how to fill out a template for an end-user (the person using creating a page from the template). Instructional text will:

Screenshot: Example of instructional text.

**Examples:**

Example 1 (unknown):
```unknown
<h1>Heading 1</h1>
```

Example 2 (none):
```none
<h1>Heading 1</h1>
```

Example 3 (unknown):
```unknown
<h2>Heading 2</h2>
```

Example 4 (none):
```none
<h2>Heading 2</h2>
```

---
