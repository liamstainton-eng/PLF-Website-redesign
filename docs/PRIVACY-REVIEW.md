# Public-source privacy review

The source package was checked for credentials, private-key markers, developer home-directory paths and personal email addresses. No such values were found in the tracked text files. Public PLF contact details, published website content and original community imagery are intentionally retained.

The separate privacy commit removes the obsolete source ZIP from the working tree, removes author/application metadata from the safeguarding PDF without changing its page text, and ignores common local credential and private-file locations. Generated WebP assets contain no EXIF/XMP metadata. New commits use the GitHub no-reply author address.

This is a targeted source/metadata review, not an assurance that all third-party published material has editorial or image-permission approval. Source testimonials and images still require the charity's review before a live launch.

Important history limitation: deleting the ZIP or changing new commit metadata does not erase earlier Git objects. The three commits that predate the editable-source PR contain a personal author email, and the old ZIP remains accessible through history. Removing that historical information requires a separately agreed history rewrite; this PR preserves the existing branch history and leaves merging to the repository owner.
